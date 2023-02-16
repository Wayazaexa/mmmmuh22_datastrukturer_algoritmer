
$$
1 < \log(n) < \sqrt{n} < n\log n < n^2 < n^3 < ... < 2^n < 3^n < ... < n^n
$$

$O$: big-oh - övre gräns

$\Omega$: big-omega - lägre gräns

$\Theta$: theta - medelgräns

$f(n)=O(g(n))$ där $g(n) = n$

Omm det finns $(\exists)$ konstanter $c$ och $n_0$ så att

$f(n) \leq c \cdot g(n)$ för någon $c$ och $n>n_0$

$f(n) = 3\cdot n + 2$

$f(n)=O(g(n))$ där $g(n) = n$

$3 \cdot n +4 \leq c \cdot g(n)$ för någon konstant $c$ och $n_0$ där $n>n_0$

Rita upp graf med $c=5$. Vi hittar $n_0=1$.

$3 \cdot n + 4 \leq 5 \cdot n$ för alla n>1

Så $f(n)$ är $O(n)$

Notera att $f(n)$ också är <br>
$O(n^2)$, $O(2^n)$ och så vidare.

På samma sätt, kan vi visa att 

$f(n) = \Omega(g(n))$

Det vill säga 

$f(n) \geq c \cdot g(n)$ 

för någon konstant tillräckligt stora n ($n > n_0$)

I det här fallet

$3 \cdot n + 4 \geq 1 \cdot n$ för alla $n>0$

Så $f(n)$ är $\Omega(n)$

Notera att $f(n)$ också är $O(1)$

Eftersom $f(n)$ är både är $O(n)$ och $\Omega(n)$ är den också $\Theta(n)$

Matematiskt:

$f(n) = \Theta(n)$ om det finns konstanter $c_1$, $c_2$ och $n_0$

$c_1\cdot g(n) \leq f(n) \leq c_2 \cdot g(n)$

för $n>n_0$