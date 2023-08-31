import Control.Monad (mapM)
import Control.Applicative ((<$>))
import Text.Parsec
import Text.Parsec.String

-- | Identity
i :: forall a. a -> a
i x = x

-- | Const.
k :: forall a b. a -> b -> a
k x _ = x

-- | Generalized version of function application.
-- s is applied to y inside the environment of z.
s :: forall a b c. (c -> b -> a) -> (c -> b) -> (c -> a)
s x y z = x z (y z)

data SKI = S | K | I | App [SKI] | Atom String deriving (Eq, Show)

parser :: Parser SKI
parser = primitive <|> atom <|> app where
    primitive :: Parser SKI
    primitive = ((char 's' <|> char 'S') >> return S)
            <|> ((char 'k' <|> char 'K') >> return K)
            <|> ((char 'i' <|> char 'I') >> return I)
    atom :: Parser SKI
    atom = fmap Atom (char '\'' >> many1 letter)
    app :: Parser SKI
    app = do
        char '(' >> spaces
        xs <- sepBy parser spaces
        spaces >> char ')'
        return $ App xs

eval :: SKI -> Either String SKI
eval S = return S
eval K = return K
eval I = return I
eval (Atom x) = return $ Atom x
eval (App xs@(Atom _:_)) = fmap App (mapM eval xs)
eval (App [I, x]) = eval x
eval (App [K, x, _]) = eval x
eval (App [S, f, g, x]) = do
    f' <- eval f
    g' <- eval g
    x' <- eval x
    eval $ App [App [f', x'], App [g', x']]
eval (App [x]) = eval x
eval (App []) = return $ App []
eval (App [S, f, g]) = do
    f' <- eval f
    g' <- eval g
    return $ App [S, f', g']
eval (App [S, f]) = do
    f' <- eval f
    return $ App [S, f']
eval (App [K, x]) = do
    x' <- eval x
    return $ App [K, x']
eval (App (S:f:g:x:t:ts)) = do
    x' <- eval $ App [S, f, g, x]
    t' <- eval t
    ts' <- mapM eval ts
    eval $ App (x':t':ts')
eval (App (K:x:_:t:ts)) = do
    x' <- eval x
    t' <- eval t
    ts' <- mapM eval ts
    eval $ App (x':t':ts')
eval (App (I:x:t:ts)) = do
    x' <- eval x
    t' <- eval t
    ts' <- mapM eval ts
    eval $ App (x':t':ts')
eval (App (xs@(App _):ts)) = do
    xs' <- eval xs
    ts' <- mapM eval ts
    case xs' of
      (App xs') -> eval $ App (xs' ++ ts')
      _         -> eval $ App (xs':ts')
val _ = error "Un expected SKI formula!"

interpret :: String -> Either String SKI
interpret code = case parse parser "SKI" code of
                   Left err  -> Left $ show err
                   Right ast -> eval ast

-- examples:
--
-- (I K)           ---> K
-- (K 'a 'b)       ---> 'a
-- (S I I 'a)      ---> ('a 'a)
-- (K (I 'a))      ---> (K 'a)
-- (S I K (I K))   ---> (K (K K))
-- (I K 'a 'b)     ---> ('a)
-- (K I S S)       ---> S
-- (I K (S I K K)) ---> (K (K (K K)))
--
-- (S I I (S I I)) ---> Non-terminating


