import sqlite3
import datetime
import logging

def getDgEbFlag():
    print 'one'
    try:
        conn = sqlite3.connect('db/dgOrEbDatabase.db')
        cur = conn.cursor()
        # print 'con ' + conn
        cur.execute('select dgEbFlag from dgEbFlagTable order by create_tmstp desc limit 1')
        dgEbFlag = cur.fetchone()[0]
    except sqlite3.Error as e:
        logging.error("DB error : %s" %e)
    except Exception as e:
        logging.error("exception in query : %s" %e)
    finally:
        if conn:
            conn.close()

 
    # conn.close()
    # logging.info('******')
    logging.info('dgorEB   ' + str(dgEbFlag))
    return dgEbFlag.encode('utf8')


def storeDgEbFlag(dgEbFlag):
    try:
        conn = sqlite3.connect('db/dgOrEbDatabase.db')
        cur = conn.cursor()
        currDate = str(datetime.datetime.now())
        data = cur.execute('insert into dgEbFlagTable values (?,?)', [dgEbFlag,currDate])
        conn.commit()
    except sqlite3.error as e:
        logging.error("db error as : %s" %e)
    except Exception as e:
        logging.error('exception as : %s' %e)
    finally:
        if conn:
            conn.close()
    # dgEbFlag =str(cur.fetchone())
    # conn.commit()
    # conn.close()
    logging.info('flag inserted ' + str(dgEbFlag) + '  curr date ' + str(currDate))

def main():
    logging.basicConfig(filename='log_dgOrEB.log',level=logging.DEBUG)
    dgEbFlag = getDgEbFlag()
    print 'flag ' + dgEbFlag
    if dgEbFlag == 'EB':
        dgEbFlag = 'DG'
    elif dgEbFlag == 'DG':
        dgEbFlag = 'EB'

    storeDgEbFlag(dgEbFlag)

    return None


if __name__ == '__main__':
    main()


    