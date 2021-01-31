package com.techlab.game;

public class ResultAnlayzer {
	
	private Result result = Result.Draw;
	private Mark[] m = {Mark.X,Mark.O};
	private int[][] win_pos = {{1,2,3},{4,5,6},{7,8,9},{1,4,7},{2,5,8},{3,6,9},{1,5,9},{3,5,7}};
	
	public void result(Mark[][] board,Board b)
	{
		Board b_map = b;
		for (int i = 0; i < m.length; i++)
		{
			for (int[] wp : win_pos)
			{
				int[] pos1 = b_map.map.get(wp[0]);
				int[] pos2 = b_map.map.get(wp[1]);
				int[] pos3 = b_map.map.get(wp[2]);
				if(m[i] == board[pos1[0]][pos1[1]] && m[i] == board[pos2[0]][pos2[1]] && m[i] == board[pos3[0]][pos3[1]])
				{
					result = Result.Win;
				}
			}
		}
	}
	public Result getResult()
	{
		return result;
	}
}
