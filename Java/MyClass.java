public class MyClass{
	public static void main(String[] args) {
		Scanner myScan = new Scanner(System.in);
		while (true)
		{
			int ans = myScan.nextLine();
			System.out.println("Enter 1 or 2:");
			switch (ans){
				case 1:
					System.out.println("This is case 1");
					break;
				case 2:
					System.out.println("This is case 2");
					break;
				default:
					System.out.println("You didn't follow the rules!");
					break;
			}
		}
	}
}