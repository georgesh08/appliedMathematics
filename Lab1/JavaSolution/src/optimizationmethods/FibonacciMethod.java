package optimizationmethods;

import static optimizationmethods.MyFunc.myFunc;

public class FibonacciMethod {
    private static double fib(int n){
        if(n <= 1){
            return n;
        }
        return fib(n-1) + fib(n-2);
    }

    private static double countX1Fib(double lowerBound, double upperBound, int n){
        double phi = fib(n-2)/fib(n);
        return lowerBound + phi * (upperBound - lowerBound);
    }

    private static double countX2Fib(double lowerBound, double upperBound, int n){
        double phi = fib(n-1)/fib(n);
        return lowerBound + phi * (upperBound - lowerBound);
    }

    public static double fibonacci(double lowerBound, double upperBound, int n){
        double prev = 1, funcCalls = 2;
        double x1 = countX1Fib(lowerBound, upperBound, n);
        double x2 = countX2Fib(lowerBound, upperBound, n);
        double funcValue1 = myFunc(x1);
        double funcValue2 = myFunc(x2);
        System.out.println("Fibonacci:");
        for(int i = 0; i < n; i++){
            System.out.println(i + " | " + Math.abs(upperBound - lowerBound) + " | "
                    + Math.abs(upperBound - lowerBound)/prev);
            prev = Math.abs(upperBound - lowerBound);
            if(funcValue1 > funcValue2){
                lowerBound = x1;
                x1 = x2;
                x2 = upperBound - (x1 - lowerBound);
                funcValue1 = funcValue2;
                funcValue2 = myFunc(x2);
                funcCalls++;
            } else if (funcValue2 > funcValue1){
                upperBound = x2;
                x2 = x1;
                x1 = lowerBound + (upperBound - x2);
                funcValue2 = funcValue1;
                funcValue1 = myFunc(x1);
                funcCalls++;
            } else {
                x1 = countX1Fib(lowerBound, upperBound, i);
                x2 = countX2Fib(lowerBound, upperBound, i);
                funcValue1 = myFunc(x1);
                funcValue2 = myFunc(x2);
                funcCalls += 2;
            }
        }
        System.out.println("\nFibonacci iterations: " + n + "\nFunc calls: " + funcCalls + "\n");
        return (lowerBound + upperBound) / 2;
    }
}
