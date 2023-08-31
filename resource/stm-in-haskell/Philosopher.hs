module Philosopher (simulate) where

import System.Random
import Control.Monad
import Control.Concurrent
import Control.Concurrent.STM
import Debug.Trace

type Semaphore = TVar Bool

newSem :: Bool -> IO Semaphore
newSem val = newTVarIO val

p :: Semaphore -> STM ()
p sem = do
    readTVar sem >>= check
    writeTVar sem False

v :: Semaphore -> STM ()
v sem = writeTVar sem True

type Buffer a = TVar [a]

newBuffer :: IO (Buffer a)
newBuffer = newTVarIO []

push :: Buffer a -> a -> STM ()
push buffer item = readTVar buffer >>= writeTVar buffer . (++ [item])

pop :: Buffer a -> STM a
pop buffer = readTVar buffer >>= \x -> case x of
    []     -> retry
    (x:xs) -> writeTVar buffer xs >> return x

output buffer = atomically (pop buffer) >>= putStrLn >> output buffer

simulate n = do
    chopsticks <- replicateM n (newSem True)
    bufout <- newBuffer
    let thead i = philosopher i (chopsticks!!i) (chopsticks!!((i+1) `mod` n))
    mapM_ (\i -> forkIO (thead i bufout)) [0..n-1]
    output bufout

philosopher :: Int -> Semaphore -> Semaphore -> Buffer String -> IO ()
philosopher n left right bufout = do
    -- thinking.
    atomically (push bufout $ "Philosopher " ++ show n ++ " is thinking.")
    randomDelay

    atomically $ do { p left; p right }

    -- eating.
    atomically (push bufout $ "Philosopher " ++ show n ++ " is eating.")
    randomDelay

    atomically $ do { v left; v right }

    -- continue.
    philosopher n left right bufout

    where randomDelay = randomRIO (100000, 500000) >>= threadDelay
