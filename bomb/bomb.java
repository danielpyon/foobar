import java.math.BigInteger;

public class bomb {

public static String solution(String x, String y) {
	BigInteger a = new BigInteger(x);
	BigInteger b = new BigInteger(y);

	int count = 0;
	while(true) {
		if (a.equals(BigInteger.ONE) && b.equals(BigInteger.ONE))
			break;
		if (a.equals(b))
			return "impossible";
		count++;
		if (a.subtract(b).compareTo(BigInteger.ZERO) > 0)
			a = a.subtract(b);
		else
			b = b.subtract(a);	
	}
	return Integer.toString(count);
}

public static void main(String[] args) {
	assert bomb.solution("7", "4") == "4";
}

}
