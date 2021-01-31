package com.techlab.game.test;

import java.util.Scanner;

import com.techlab.game.Board;
import com.techlab.game.Result;
import com.techlab.game.ResultAnlayzer;

public class GameTest {
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		boolean flag = true;
		boolean mark_pos_val = true;
		int counter = 0;
		int pos;
		Result result = null;
		while(flag == true)
		{
			System.out.println("1:Game"+"\n"+"2:End");
			System.out.print("Enter Choice: ");
			int num = sc.nextInt();
			switch(num)
			{
				case 1:
					System.out.print("Enter Player1: ");
					String p1 = sc.next();
					System.out.print("Enter Player2: ");
					String p2 = sc.next();
					System.out.println();
					Board b = new Board();
					ResultAnlayzer ra = new ResultAnlayzer();
					while(counter < 9)
					{
						if(counter%2==0)
						{
							System.out.print(p1+" turn: ");
							pos = sc.nextInt();
							mark_pos_val = b.markPos(pos, counter);
							if(mark_pos_val == false)
								break;
							b.printBoard();
							ra.result(b.getBoard(), b);
							result = ra.getResult();
						}
						else
						{
							System.out.print(p2+" turn: ");
							pos = sc.nextInt();
							mark_pos_val = b.markPos(pos, counter);
							if(mark_pos_val == false)
								break;
							b.printBoard();
							ra.result(b.getBoard(), b);
							result = ra.getResult();
						}
						if(result == Result.Win)
						{
							break;
						}
						counter++;
					}
					if(mark_pos_val == false)
					{
						
					}
					else if(result == Result.Win)
					{
						if(counter%2==0)
						{
							System.out.println(p1+" "+Result.Win);
						}
						else
						{
							System.out.println(p2+" "+Result.Win);
						}
					}
					else
					{
						System.out.println(Result.Draw);
					}
					System.out.println();
					counter = 0;
					break;
				case 2:
					flag = false;
					break;
			}
			}
		}

}
