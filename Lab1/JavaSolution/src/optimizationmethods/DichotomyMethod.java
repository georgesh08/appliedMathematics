package optimizationmethods;

import static optimizationmethods.MyFunc.myFunc;

public class DichotomyMethod {
    public static double dichotomy(double eps, double lowerBound, double upperBound){
        double x1, x2, counter, prev;
        double delta = eps/3;
        counter = 0;
        prev = 1;
        System.out.println("Dichotomy:");
        while(true){
            if(upperBound - lowerBound < eps){
                return (upperBound + lowerBound)/2;
            }
            System.out.println(counter++ + " | " + Math.abs(upperBound - lowerBound) + " | "
                    + Math.abs(upperBound - lowerBound)/prev);
            prev = Math.abs(upperBound - lowerBound);
            x1 = (lowerBound + upperBound) / 2 - delta;
            x2 = (lowerBound + upperBound) / 2 + delta;
            double funcValue1 = myFunc(x1);
            double funcValue2 = myFunc(x2);
            if (funcValue1 < funcValue2) {
                upperBound = x2;
            } else if (funcValue1 > funcValue2) {
                lowerBound = x1;
            } else {
                lowerBound = x1;
                upperBound = x2;
            }
        }
    }
}
