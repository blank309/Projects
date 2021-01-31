package com.techlab.game;

import java.util.HashMap;

public class CustomException {
	public static void validate(int num,HashMap<Integer,int[]> map,Mark[][] board)throws SamePosnException
	{
		int[] pos = map.get(num);
		if(board[pos[0]][pos[1]] != null)
		{
			throw new SamePosnException("Cannot Insert at Same Position");
		}
	}
}
