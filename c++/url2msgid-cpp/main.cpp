

#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <fstream>
#include <sstream>

#include "bignumber.h"
#include "MyBigNumber.h"
#include "CharIdMap.h"
#include "Url2Msgid.h"

using namespace std;


int main()
{
	CharIdMap::init();
	printf ("-----start test ------\n");
	for (int k=0; k<100000000L;k++)
	{
		printf("LOOP %d ..... \n", k);
		for (int i=0; i<10000; i++)
		{
			
			const char* url1 = "/fs/fhfs/v1/u6b3/20170908/http/SXYved/5527/1729672/89869";
			std::string msgid = Url2Msgid::encode(url1);
			std::string url2 = Url2Msgid::decode(msgid.c_str());
			//printf("url1=%s \n", url1);
			//printf("msgid=%s \n", msgid.c_str());
			//printf("url2=%s \n", url2.c_str());
			if (url2 == url1){
				//printf("correct\n");
			}else{
				printf("wrong !!!-----\n");
			}
		}
	}
}


int main1()
{
	CharIdMap::init();
	printf ("-----start test ------\n");
			/*
		 * 程序输出：
/fs/fhfs/v1/u6b3/20170908/http/SXYved/5527/1729672/89869
v1GCOWOa9wo1J1wPDZVRQdlnSzj3m12Z4WxoqMfbCNKHfJocxjyDjuDScbcit
/fs/fhfs/v1/u6b3/20170908/http/SXYved/5527/1729672/89869
correct
		 */

	
	const char* url1 = "/fs/fhfs/v1/u6b3/20170908/http/SXYved/5527/1729672/89869";
	std::string msgid = Url2Msgid::encode(url1);
	std::string url2 = Url2Msgid::decode(msgid.c_str());
	printf("url1=%s \n", url1);
	printf("msgid=%s \n", msgid.c_str());
	printf("url2=%s \n", url2.c_str());
	if (url2 == url1){
		printf("correct\n");
	}else{
		printf("wrong !!!-----\n");
	}
}

