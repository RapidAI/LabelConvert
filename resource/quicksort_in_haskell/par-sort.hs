-- | Parallel quicksort.

import Control.Monad
import Control.Monad.ST (ST (..), runST)
import Data.Array.ST
import Control.Parallel.Strategies

qsortImpl :: (Integral i, Ix i, Ord e, MArray arr e m) => arr i e -> i -> i -> m ()
qsortImpl arr l r = when (r > l) $ do
    let mid = l + (r - l) `div` 2
    nmid <- partition arr l r mid
    withStrategy rpar $ qsortImpl arr l (nmid - 1)
    qsortImpl arr (nmid + 1) r

partition :: (Integral i, Ix i, Ord e, MArray arr e m) => arr i e -> i -> i -> i -> m i
partition arr l r mid = do
    pivot <- readArray arr mid
    swap arr mid r
    slot <- foreach [l..r-1] l (\slot i -> do
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

foreach :: (Monad m, Foldable t) => t a -> b -> (b -> a -> m b) -> m b
foreach xs v f = foldM f v xs

qsort :: [Int] -> [Int]
qsort xs = runST $ do
    let len = length xs - 1
    arr <- newListArray (0, len) xs :: ST s (STArray s Int Int)
    qsortImpl arr 0 len >> getElems arr

main = print $ qsort [1,3,5,7,9,2,4,6,8,0]

