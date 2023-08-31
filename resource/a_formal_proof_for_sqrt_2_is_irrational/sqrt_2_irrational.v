(** Proof for the fact that square root of 2 is irrational. **)

Require Import Reals.Reals.
Require Import Bool.
(* Require Import Natural.Peano.NPeano.
*)

(* Count tailing zeros for positive type. *)
Fixpoint ctz_Pos (x : positive) : nat :=
  match x with
    | xH   => O                            (* 1 *)
    | xO t => S (ctz_Pos t)   (* t ~ 0 *)
    | xI t => O                            (* t ~ 1 *)
  end.

(* Lift to Z. *)
Definition ctz_Z (x : Z) : nat :=
  match x with
    | Z0     => O
    | Zpos t => ctz_Pos t
    | Zneg t => ctz_Pos t
  end.

(* If x = a * 2^k, then 2*x = a * 2^(k+1). *)
Lemma double_inc_ctz :
  forall x, (x <> 0%Z) -> ctz_Z (2 * x) = S (ctz_Z x).
Proof.
  destruct x; intuition || intro; reflexivity.
Qed.

(* For a suqare number, even_repeat(x) must be even. *)
Lemma square_ctz_even :
  forall x : Z, Nat.even (ctz_Z (x * x)) = true.
Proof.
  (* At first, prove the positive case. *)
  assert (hypothesis_positive : forall k : positive, Nat.even (ctz_Pos (k * k)) = true).
  + induction k.
    - reflexivity.
    - simpl; rewrite Pos.mul_comm; simpl; assumption.
    - reflexivity.
  + destruct x; simpl; rewrite hypothesis_positive || idtac; reflexivity.
Qed.

Lemma cannot_both_even :
  forall x, Nat.even x = negb (Nat.even (S x)).
Proof.
  induction x.
  + reflexivity.
  + simpl (Nat.even (S (S x))).
    rewrite IHx; rewrite negb_involutive; reflexivity.
Qed.

Lemma sqrt_mult_sqrt_eq_n :
  forall x : R, (0 <= x)%R -> (sqrt x * sqrt x)%R = x.
Proof.
  apply sqrt_def.
Qed.

Definition irrational (x : R) : Prop :=
  ~ exists p q : Z, (q > 0)%Z /\ (IZR p / IZR q)%R = x.

Theorem sqrt_2_irrational :
  irrational (sqrt 2%R)%R.
Proof.
  unfold irrational.
  (* Get two hypotheses, and now we need to find the contradiction (proof "False"). *)
  intros [p [q [q_gt_0_Z p'q_eq_sqrt_2_R]]].

  (* To be proved: "p*p = 2*q*q". *)

  assert (q_gt_0_R : (IZR q > 0)%R).
    replace 0%R with (IZR 0).
    apply Rlt_gt; apply IZR_lt; auto with zarith.
    reflexivity.

  assert (p_eq_sqrt_2_q_R : (IZR p = sqrt 2 * IZR q)%R).
    rewrite <- p'q_eq_sqrt_2_R.
    field; apply Rgt_not_eq; apply q_gt_0_R.

  assert (pp_eq_2qq_R : (IZR p * IZR p = (sqrt 2 * IZR q) * (sqrt 2 * IZR q))%R).
    rewrite <- p_eq_sqrt_2_q_R; reflexivity. (* Or use "congruence". *)

  assert (pp_eq_2qq_Z : (p * p = 2 * q * q)%Z).
    replace ((sqrt 2 * IZR q) * (sqrt 2 * IZR q))%R
      with ((sqrt 2 * sqrt 2) * IZR q * IZR q)%R
      in pp_eq_2qq_R
      by ring.
    rewrite sqrt_def in pp_eq_2qq_R
      by auto with real.
    replace 2%R with (IZR 2) in pp_eq_2qq_R
      by reflexivity.
    repeat rewrite <- mult_IZR in pp_eq_2qq_R.
    apply eq_IZR; assumption.

  (* Counting tailing zeros for "p*p" and "q*q". *)

  assert (ctz_p : Nat.even (ctz_Z (p * p)) = true).
    apply square_ctz_even.
  assert (ctz_q : Nat.even (ctz_Z (q * q)) = true).
    apply square_ctz_even.

  assert (ctz_p_eq_S_ctz_q : ctz_Z (p*p) = S (ctz_Z (q * q))).
    rewrite <- double_inc_ctz.
    rewrite pp_eq_2qq_Z; rewrite Z.mul_assoc; reflexivity.
    assert (q*q > 0)%Z.
      auto with zarith.
    auto with zarith.

  rewrite ctz_p_eq_S_ctz_q in ctz_p.
  rewrite cannot_both_even in ctz_q.
  rewrite ctz_p in ctz_q; inversion ctz_q.
Qed.


