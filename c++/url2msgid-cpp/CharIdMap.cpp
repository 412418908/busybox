

#include <sstream>
#include <stack>
#include <iostream>
#include <stdlib.h>
#include <string.h>

#include "common.h"
#include "CharIdMap.h"

	CharIdMap* CharIdMap::gUrlMap = NULL;
	CharIdMap* CharIdMap::gMsgIdMap = NULL;
	
	void CharIdMap::init()
	{
		const char* s1 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-/:_+@#$%^&?=;";
		gUrlMap =  new CharIdMap(s1, strlen(s1));
		
		const char* s2 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
		gMsgIdMap = new CharIdMap(s2, strlen(s2));
	}
	
	CharIdMap::CharIdMap(const char* charStr, int radix):mRadix(radix)
	{
		memset(mId2Char,0, sizeof(mId2Char));
		memset(mChar2Id,0, sizeof(mChar2Id));
		int len = strlen(charStr);
		for (int i=0; i<len; i++){
			uint8 ch = (uint8)charStr[i];
			mId2Char[i] = ch;
			mChar2Id[ch] = i;
		}
	}
		
	
	int CharIdMap::idOfChar(char ch)
	{
		 return mChar2Id[(int)ch];
	}
	
	char CharIdMap::charOfId(int id)
	{
		return mId2Char[id];
	}
	
		