import java.util.Arrays;
import java.util.Scanner;

public class BubbleSort {
	
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		System.out.print("Type the size of the Array: ");
		int x = input.nextInt();
		
		int[] array = new int[x];
		
		// filling the array
		for(int i = 0; i < array.length; i++) {
			int a = input.nextInt();
			array[i] = a;
		}
		
		// sort the array
		int aux = 0;
		for(int i = 0; i < array.length; i++) {
			for (int j = 0; j < (array.length - 1); j ++) {
				if (array[j] > array[j + 1]) {
					aux = array[j];
					array[j] = array[j + 1];
					array[j + 1] = aux;
				}
			}
		}
		System.out.println(Arrays.toString(array));
	}
}
