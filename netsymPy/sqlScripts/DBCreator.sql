CREATE TABLE "rules_tbl" (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`selIntface`	TEXT,
	`txtBufferLimit`	TEXT,
	`txtBandwidth`	TEXT,
	`selDelayDistribution`	TEXT,
	`txtDelay`	TEXT,
	`txtDelayJitter`	TEXT,
	`txtDelayCorrelation`	TEXT,
	`txtReorder`	TEXT,
	`txtReorderCorrelation`	TEXT,
	`txtGap`	TEXT,
	`txtLoss`	TEXT,
	`txtLossCorrelation`	TEXT,
	`txtDup`	TEXT,
	`txtDupCorrelation`	TEXT,
	`txtCurp`	TEXT,
	`txtCurptionCorrelation`	TEXT,
	`portSrc`	TEXT,
	`portDst`	TEXT,
	`macSrc`	TEXT,
	`macDest`	TEXT,
	`flowlabelTOS`	TEXT,
	`transport`	TEXT,
	`transportPrtc`	TEXT,
	`ipSrc`	TEXT,
	`ipSrcSub`	TEXT,
	`ipDest`	TEXT,
	`ipDestSub`	TEXT,
	`ipVer`	TEXT,
	`ruleStatus`	TEXT );
/* */
 INSERT INTO `rules_tbl` (id,selIntface,txtBufferLimit,txtBandwidth,selDelayDistribution,
						 txtDelay,txtDelayJitter,txtDelayCorrelation,txtReorder,txtReorderCorrelation,
						 txtGap,txtLoss,txtLossCorrelation,txtDup,txtDupCorrelation,txtCurp,
						 txtCurptionCorrelation,portSrc,portDst,macSrc,macDest,flowlabelTOS,
						 transport,transportPrtc,ipSrc,ipSrcSub,ipDest,ipDestSub,ipVer,ruleStatus)
						 VALUES (1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,
						 NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/* */
 DELETE FROM "sqlite_sequence";
/* */
 INSERT INTO "sqlite_sequence" VALUES('rules_tbl',2);
