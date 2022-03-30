import static optimizationmethods.BrentMethod.brent;
import static optimizationmethods.DichotomyMethod.dichotomy;
import static optimizationmethods.FibonacciMethod.fibonacci;
import static optimizationmethods.GoldenRatioMethod.goldenRatio;
import static optimizationmethods.ParabolaMethod.parabola;

public class Main {
    public static void main(String[] args) {
        double res = dichotomy(1e-3, 6, 9);
        double res1 = goldenRatio(1e-3, 6, 9);
        double res2 = fibonacci(6, 9, 19);
        double res3 = parabola(1e-3, 6, 9);
        double res4 = brent(1e-3, 3, 13);
        System.out.println("Dichotomy result: " + res);
        System.out.println("Golden ratio result: " + res1);
        System.out.println("Fibonacci result: " + res2);
        System.out.println("Parabola search: " + res3);
        System.out.println("Brent search: " + res4);
    }
}
