{-# LANGUAGE FlexibleContexts #-}

-- | Concurrent quicksort with `forkIO`.

import Control.Monad
import Data.Array.IO
import Control.Concurrent

qsortImpl arr l r = when (r > l) $ do
    let mid = l + (r - l) `div` 2
    nmid <- partition arr l r mid
    dualThread (qsortImpl arr l (nmid - 1))
             (qsortImpl arr (nmid + 1) r)
    where
        dualThread fg bg = do
            wait <- backgroud bg
            fg >> wait
        backgroud task = do
            m <- newEmptyMVar
            forkIO (task >>= putMVar m)
            return $ takeMVar m

partition :: (Integral i, Ix i, Ord e, MArray arr e m) => arr i e -> i -> i -> i -> m i
partition arr l r mid = do
    pivot <- readArray arr mid
    swap arr mid r
    slot <- foreachWith [l..r-1] l (\slot i -> do
        val <- readArray arr i
        if val < pivot
           then swap arr i slot >> return (slot+1)
           else return slot)
    swap arr slot r >> return slot

swap :: (Ix i, MArray arr e m) => arr i e -> i -> i -> m ()
swap arr ia ib = do
    a <- readArray arr ia
    b <- readArray arr ib
    writeArray arr ia b
    writeArray arr ib a

foreachWith :: (Monad m, Foldable t) => t a -> b -> (b -> a -> m b) -> m b
foreachWith xs v f = foldM f v xs

qsort :: [Int] -> IO [Int]
qsort xs = do
    let len = length xs - 1
    arr <- newListArray (0, len) xs :: IO (IOArray Int Int)
    qsortImpl arr 0 len >> getElems arr

main = qsort [1,3,5,7,9,2,4,6,8,0] >>= print


