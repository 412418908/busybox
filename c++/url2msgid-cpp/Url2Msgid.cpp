

#include <sstream>
#include <stack>
#include <iostream>
#include <stdlib.h>
#include <string.h>

#include "common.h"
#include "Url2Msgid.h"
#include "CharIdMap.h"
#include "MyBigNumber.h"

	std::string Url2Msgid::encode(const char* url1)
	{
		if (strstr(url1, "http://") == url1){
			printf("you must remove http://ip:port first \n");
			return "";
		}
		std::string url = "1";
		url.append(url1);
		MyBigNumber urlNum(CharIdMap::gUrlMap->getRadix());
		MyBigNumber::string2Number(url, *CharIdMap::gUrlMap, urlNum);
		MyBigNumber msgidNum(urlNum, CharIdMap::gMsgIdMap->getRadix());
		
		std::string result;
		result.append("v1");
		result.append(MyBigNumber::number2String(msgidNum, *CharIdMap::gMsgIdMap) );
		return result;
	}
	
	std::string Url2Msgid::decode(const char* msgid)
	{
		
		if (strstr(msgid, "v1") != msgid){
			printf("msgid must start with v1, your value is :%s\n", msgid);
			return "";
		}
		std::string msgidStr = (const char*)(msgid + 2);
		MyBigNumber msgidNum(CharIdMap::gMsgIdMap->getRadix());
		MyBigNumber::string2Number(msgidStr, *CharIdMap::gMsgIdMap, msgidNum);
		MyBigNumber urlNum(msgidNum, CharIdMap::gUrlMap->getRadix());
		std::string result = MyBigNumber::number2String(urlNum, *CharIdMap::gUrlMap);
		return result.substr(1);
		
		
	}
	
	
		