package com.techlab.game;

import java.util.HashMap;



public class Board {
	private Mark[][] board = new Mark[3][3];
	HashMap<Integer,int[]> map=new HashMap<Integer,int[]>();
	
	public Board()
	{
		int num = 0;;
		System.out.println("Game Started:");
		printBoard();
		for (int i = 0; i < 3; i++)
		{
			for (int j = 0; j < 3; j++)
			{
				num = num + 1;
				map.put(num, new int[] {i,j});
			}
		}
	}
	
	public void printBoard()
	{
		for (int i = 0; i < 3; i++)
		{
			for (int j = 0; j < 3; j++)
			{
				System.out.print(board[i][j]+" ");
			}
			System.out.println();
		}
		System.out.println();
	}
	
	public boolean markPos(int num,int counter)
	{
		try
		{
			int[] ar = map.get(num);
			CustomException.validate(num,map,board);
			if(counter%2==0)
			{
				board[ar[0]][ar[1]] = Mark.X;
			}
			if(counter%2!=0)
			{
				board[ar[0]][ar[1]] = Mark.O;
			}
			return true;
		}
		catch(Exception m)
		{
			System.err.println(m);
			return false;
		}
		
	}
	
	public Mark[][] getBoard()
	{
		return board;
	}
}
