URI: Unified Ressource Locator
PRM: Parametre
TYP: Type

 

TABLE URI, Jonction from URL to HASH
                URI_ID,URI-HSH_ID,URI
                1,3,http://ec.europa.eu/taxation_customs/dds2/seed/help/index.jsp

 

TABLE URI-HSH, Chronology info on a URL
                URI-HSH_ID,URI_HSH,LASTSEEN,FIRSTSEEN
                3,b836b1037869e9414dbc338005bbe91c,2012-08-06,2003-08-06

 

TABLE PRM, Param Name list
                PRM_ID,PRM
                5,"lang"

 

TABLE URI-PRM ,JONCTION form URI to Parametre
                URI-PRM_ID,URI-HSH_ID,PRM_ID,LASTSEEN,FIRSTSEEN,COUNT
                9,3,5,2012-08-06,2003-08-06,12321

 

TABLE URI-PRM-TYP, Jonction parametre-uri et val uri
                URI-PRM-TYP_ID,URI-PRM_ID,PRM-TYP_ID,LASTSEEN,FIRSTSEEN,COUNT
                13,9,11,2012-08-06,2003-08-06,12321

 

TABLE URI-PRM-SIZE, Jonction parametre-uri et taille uri
                URI-PRM-SIZE_ID,URI-PRM_ID,SIZE_MIN,SIZE_MAX,SIZE_MOY
                15,9,1,5,3

 

TABLE PRMTYPE
                PRM-TYP_ID,REGEX, DESC
                11,"^0|1$","Binary 0 or 1"
                11,"^true|false$", "Binary true or false"
                11,"(^[a-z]{2}$)", "Two letters"
                11,"^[A-Z]{2}$", "Two letters
                11,"^[0-9]{1,}$"
                11,"^[a-zA-Z]{1,}$"
                11,"^[a-z0-9]{1,}$"
                11,"^[a-zA-Z0-9]{1,}$"
                11,"^[a-z0-9]{1,}$"
                11,"^[0-9]{1,}$"
                11,"^[a-zA-Z]{1,}$"
                11,"^[a-z0-9]{1,}$"
                11,"^[a-zA-Z0-9]{1,}$"
                11,"^[a-z0-9]{1,}$"
               
               
