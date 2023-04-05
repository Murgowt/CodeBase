package proj1;  

/**
 * Models a plastic roll-a-coin bank from the 1980s
 * 
 * @author
 * @version
 *
 */
public class Coinbank {
	
	// Denominations
	public static final int PENNY_VALUE = 1;
	public static final int NICKEL_VALUE = 5;
	public static final int DIME_VALUE = 10;
	public static final int QUARTER_VALUE = 25;
	
	//Renaming the variables to meaningful names 
	private final int PENNY_INDEX = 0;
	private final int NICKEL_INDEX = 1;
	private final int DIME_INDEX = 2;
	private final int QUARTER_INDEX = 3;
	
	// number of types of coins the bank holds
	private final int COINTYPES = 4;
	
	private int[] holder;
	
	/**
	 * Default constructor
	 */
	public Coinbank() {
		//Initializing all coin's count to zero
		holder = new int[COINTYPES];
		holder[PENNY_INDEX]=0;
		holder[NICKEL_INDEX]=0;
		holder[DIME_INDEX]=0;
		holder[QUARTER_INDEX]=0;
	}
	
	/**
	 * getter
	 * @param coinType denomination of coin to get. Valid denominations are 1,5,10,25
	 * @return number of coins that bank is holding of that type, or -1 if denomination not valid
	 */
	public int get(int coinType){
		//Checking if the coin is Bankable
		//if yes, returning the number of coins of the corresponding denomination
		if (isBankable(coinType)) {
			if (coinType == PENNY_VALUE) {
				return holder[PENNY_INDEX];
			}
			else if (coinType == NICKEL_VALUE) {
				return holder[NICKEL_INDEX];
			}
			else if (coinType == DIME_VALUE) {
				return holder[DIME_INDEX];
			}
			else {  // coinType == QUARTER_VALUE
				return holder[QUARTER_INDEX];
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
		//Checking if the coin is Bankable
		//if yes, setting the number of coins of the corresponding denomination
		if (numCoins >= 0 && isBankable(coinType)) {
			if (coinType == PENNY_VALUE) {
				holder[PENNY_INDEX] = numCoins;
			}
			else if (coinType == NICKEL_VALUE) {
				holder[NICKEL_INDEX] = numCoins;
			}
			else if (coinType == DIME_VALUE) {
				holder[DIME_INDEX] = numCoins;
			}
			else {  // coinType == QUARTER_VALUE
				holder[QUARTER_INDEX] = numCoins;
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
	 * @param coinType either 1, 5, 10, or 25 to be valid
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
		// Initially we remove zero coins
		int removedCoins = 0;
		if (isBankable(coinType) && requestedCoins >= 0) {

			int coinsWeHave;  // coins we have before removal
			int coinsLeft;    // coins we have after removal
			//Checking the coin type and updating the remaining coins of the corresponding value
			if (coinType == PENNY_VALUE) {
				coinsWeHave = get(PENNY_VALUE);
				coinsLeft = numLeft(requestedCoins, get(PENNY_VALUE));
				set(PENNY_VALUE, coinsLeft);
			}
			else if (coinType == NICKEL_VALUE) {
				coinsWeHave = get(NICKEL_VALUE);
				coinsLeft = numLeft(requestedCoins, get(NICKEL_VALUE));
				set(NICKEL_VALUE,coinsLeft);
			}
			else if (coinType == DIME_VALUE) {
				coinsWeHave = get(DIME_VALUE);
				coinsLeft = numLeft(requestedCoins, get(DIME_VALUE));
				set(DIME_VALUE,coinsLeft);
			}
			else {  //coinType == QUARTER_VALUE
				coinsWeHave = get(QUARTER_VALUE);
				coinsLeft = numLeft(requestedCoins, get(QUARTER_VALUE));
				set(QUARTER_VALUE,coinsLeft);
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
