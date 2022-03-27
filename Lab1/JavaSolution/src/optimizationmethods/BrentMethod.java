package optimizationmethods;

import static optimizationmethods.MyFunc.myFunc;

public class BrentMethod {
    private static final double phi = (3 - Math.sqrt(5)) / 2;

    private static double countRatio(double lowerBound, double upperBound){
        return lowerBound + phi*(upperBound - lowerBound);
    }

    public static double brent(double eps, double a, double c){
        return 0;
    }
}
