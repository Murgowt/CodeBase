/**
 * JUnit test class.  Use these tests as models for your own.
 */
import org.junit.Test;
import org.junit.rules.Timeout;
import static org.junit.Assert.*;

import org.junit.Rule;

import proj1.Coinbank;

public class CoinbankTest {
	
	@Rule // a test will fail if it takes longer than 1/10 of a second to run
 	public Timeout timeout = Timeout.millis(100); 

	/**
	 * Sets up a bank with the given coins
	 * @param pennies number of pennies you want
	 * @param nickels number of nickels you want
	 * @param dimes number of dimes you want
	 * @param quarters number of quarters you want
	 * @return the Coinbank filled with the requested coins of each type
	 */
	private Coinbank makeBank(int pennies, int nickels, int dimes, int quarters) {
		Coinbank c = new Coinbank();
		int[] money = new int[]{pennies, nickels, dimes, quarters};
		int[] denom = new int[]{1,5,10,25};
		for (int index=0; index<money.length; index++) {
			int numCoins = money[index];
			for (int coin=0; coin<numCoins; coin++) {
				c.insert(denom[index]);
			}
		}
		return c;
	}

	@Test // bank should be empty upon construction
	public void testConstruct() {
		Coinbank emptyDefault = new Coinbank();
		assertEquals(0, emptyDefault.get(1));
		assertEquals(0, emptyDefault.get(5));
		assertEquals(0, emptyDefault.get(10));
		assertEquals(0, emptyDefault.get(25));
	}
	
	@Test // inserting penny should return true & one nickel should be in bank
	public void testInsertPenny_return()
	{
		Coinbank c = new Coinbank();
		assertTrue(c.insert(1));
		assertEquals(1,c.get(1));
	}
	@Test // inserting nickel should return true & one nickel should be in bank
	public void testInsertNickel_return()
	{
		Coinbank c = new Coinbank();
		assertTrue(c.insert(5));
		assertEquals(1,c.get(5));
	}
	@Test // inserting dime should return true & one nickel should be in bank
	public void testInsertDime_return()
	{
		Coinbank c = new Coinbank();
		assertTrue(c.insert(10));
		assertEquals(1,c.get(10));
	}
	@Test // inserting quater should return true & one nickel should be in bank
	public void testInsertQuater_return()
	{
		Coinbank c = new Coinbank();
		assertTrue(c.insert(25));
		assertEquals(1,c.get(25));
	}
	@Test // inserting invalid coin type should return false & one nickel should be in bank
	public void testInsertInvalidCoinType_return()
	{
		Coinbank c = new Coinbank();
		assertFalse(c.insert(42));

	}


	@Test // getter should return correct values
	public void testGet()
	{
		Coinbank c = makeBank(0,2,15,1);
		assertEquals(0,c.get(1));
		assertEquals(2,c.get(5));
		assertEquals(15,c.get(10));
		assertEquals(1,c.get(25));
		assertEquals(-1,c.get(43));
	}


	@Test // getter should not alter the bank
	public void testGet_contents()
	{
		Coinbank c = makeBank(0,2,15,1);
		c.get(1);
		c.get(5);
		c.get(10);
		c.get(25);
		String expected = "The bank currently holds $1.85 consisting of \n0 pennies\n2 nickels\n15 dimes\n1 quarters\n";
		assertEquals(expected,c.toString());
	}

	@Test // test of remove
	public void testRemove_justEnough()
	{
		Coinbank c = makeBank(4,1,3,5);
		assertEquals(5,c.remove(25,5));
		String expected = "The bank currently holds $0.39 consisting of \n4 pennies\n1 nickels\n3 dimes\n0 quarters\n";
		assertEquals(expected,c.toString());
	}
	@Test // test of remove
	public void testRemove_penny()
	{
		Coinbank c = makeBank(4,1,3,1);
		assertEquals(4,c.remove(1,4));
		String expected = "The bank currently holds $0.6 consisting of \n0 pennies\n1 nickels\n3 dimes\n1 quarters\n";
		assertEquals(expected,c.toString());
	}
	@Test // test of remove
	public void testRemove_quater()
	{
		Coinbank c = makeBank(4,1,3,1);
		assertEquals(1,c.remove(25,1));
		String expected = "The bank currently holds $0.39 consisting of \n4 pennies\n1 nickels\n3 dimes\n0 quarters\n";
		assertEquals(expected,c.toString());
	}
	@Test // test of remove
	public void testRemove_nickel()
	{
		Coinbank c = makeBank(4,1,3,1);
		assertEquals(1,c.remove(5,1));
		String expected = "The bank currently holds $0.59 consisting of \n4 pennies\n0 nickels\n3 dimes\n1 quarters\n";
		assertEquals(expected,c.toString());
	}
	@Test // test of remove
	public void testRemove_dime()
	{
		Coinbank c = makeBank(4,1,3,1);
		assertEquals(3,c.remove(10,3));
		String expected = "The bank currently holds $0.34 consisting of \n4 pennies\n1 nickels\n0 dimes\n1 quarters\n";
		assertEquals(expected,c.toString());
	}
	@Test // remove should not do anything if a 3-cent coin is requested
	public void testRemove_invalidCoin()
	{
		Coinbank c = makeBank(4,1,3,5);
		assertEquals(0,c.remove(3,1));
	}
}
