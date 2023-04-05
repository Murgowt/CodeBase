package original;

/**
 * Models a plastic roll-a-coin bank from the 1980s
 * 
 * @author Chris Fernandes
 * @version 8/29/17
 *
 */
public class Coinbank {

	// Denominations
	public static final int PENNY_VALUE = 1;
	public static final int NICKEL_VALUE = 5;
	public static final int DIME_VALUE = 10;
	public static final int QUARTER_VALUE = 25;
	
	// number of coins the bank is holding
	private int pennies;
	private int nickels;
	private int dimes;
	private int quarters;
	
	/**
	 * Default constructor
	 */
	public Coinbank() {
		pennies = 0;
		nickels = 0;
		dimes = 0;
		quarters = 0;
	}
	
	/**
	 * getter
	 * @param coinType denomination of coin to get. Valid denominations are 1,5,10,25
	 * @return number of coins that bank is holding of that type, or -1 if denomination not valid
	 */
	public int get(int coinType){
		if (isBankable(coinType)) {
			if (coinType == PENNY_VALUE) {
				return pennies;
			}
			else if (coinType == NICKEL_VALUE) {
				return nickels;
			}
			else if (coinType == DIME_VALUE) {
				return dimes;
			}
			else {  // coinType == QUARTER_VALUE
				return quarters;
			}
		}
		else {
			return -1;
		}
	}
	
	/**
	 * setter
	 * @param coinType denomination of coin to set
	 * @param numCoins number of coins
	 */
	private void set(int coinType, int numCoins) {
		if (numCoins >= 0 && isBankable(coinType)) {
			if (coinType == PENNY_VALUE) {
				pennies = numCoins;
			}
			else if (coinType == NICKEL_VALUE) {
				nickels = numCoins;
			}
			else if (coinType == DIME_VALUE) {
				dimes = numCoins;
			}
			else {  // coinType == QUARTER_VALUE
				quarters = numCoins;
			}
		}
	}

	/**
	 * Return true if given coin can be held by this bank.  Else false.
	 * @param coin penny, nickel, dime, or quarter is bankable.  All others are not.
	 * @return true if bank can hold this coin, else false
	 */
	private boolean isBankable(int coin){
		switch (coin) {
		case PENNY_VALUE: case NICKEL_VALUE: 
		case DIME_VALUE: case QUARTER_VALUE:
			return true;
		default: 
			return false;
		}
	}
	
	/** 
	 * insert valid coin into bank.  Returns true if deposit
	 * successful (i.e. coin was penny, nickel, dime, or quarter).
	 * Returns false if coin not recognized
	 * 
	 * @param coin either 1, 5, 10, or 25 to be valid
	 * @return true if deposit successful, else false
	 */
	public boolean insert(int coinType){
		if (!isBankable(coinType)) {
			return false;
		}
		else {
			set(coinType, get(coinType)+1);
			return true;
		}
	}
	
	/**
	 * returns the requested number of the requested coin type, if possible.
	 * Does nothing if the coin type is invalid.  If bank holds
	 * fewer coins than is requested, then all of the coins of that
	 * type will be returned.
	 * @param coinType either 1, 5, 10, or 25 to be valid
	 * @param requestedCoins number of coins to be removed
	 * @return number of coins that are actually removed
	 */
	public int remove(int coinType, int requestedCoins) {
		int removedCoins = 0;
		if (isBankable(coinType) && requestedCoins >= 0) {

			int coinsWeHave;  // coins we have before removal
			int coinsLeft;    // coins we have after removal
			
			if (coinType == PENNY_VALUE) {
				coinsWeHave = pennies;
				coinsLeft = numLeft(requestedCoins, pennies);
				pennies = coinsLeft;
			}
			else if (coinType == NICKEL_VALUE) {
				coinsWeHave = nickels;
				coinsLeft = numLeft(requestedCoins, nickels);
				nickels = coinsLeft;
			}
			else if (coinType == DIME_VALUE) {
				coinsWeHave = dimes;
				coinsLeft = numLeft(requestedCoins, dimes);
				dimes = coinsLeft;
			}
			else {  //coinType == QUARTER_VALUE
				coinsWeHave = quarters;
				coinsLeft = numLeft(requestedCoins, quarters);
				quarters = coinsLeft;
			}
			
			// how many coins actually got removed?
			removedCoins = coinsWeHave - coinsLeft;
		}
		return removedCoins;
	}
	

	/**
	 * returns number of coins remaining after removing the
	 * requested amount.  Returns zero if requested amount > what we have
	 * @param numWant number of coins to be removed
	 * @param numHave number of coins you have
	 * @return number of coins left after removal
	 */
	private int numLeft(int numWant, int numHave){
		return Math.max(0, numHave-numWant);
	}
	
	/**
	 * Returns bank as a printable string
	 */
	public String toString() {
		double total = (get(PENNY_VALUE) * PENNY_VALUE +
				get(NICKEL_VALUE) * NICKEL_VALUE + 
				get(DIME_VALUE) * DIME_VALUE +
				get(QUARTER_VALUE) * QUARTER_VALUE) / 100.0;
				
		String toReturn = "The bank currently holds $" + total + " consisting of \n";
		toReturn+=get(PENNY_VALUE) + " pennies\n";
		toReturn+=get(NICKEL_VALUE) + " nickels\n";
		toReturn+=get(DIME_VALUE) + " dimes\n";
		toReturn+=get(QUARTER_VALUE) + " quarters\n";
		return toReturn;
	}
}
