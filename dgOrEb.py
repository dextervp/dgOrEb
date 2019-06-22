import sqlite3
import datetime
import logging

def getDgEbFlag():
    print 'one'
    conn = sqlite3.connect('db/dgOrEbDatabase.db')
    cur = conn.cursor()
    # print 'con ' + conn
    cur.execute('select dgEbFlag from dgEbFlagTable order by create_tmstp desc limit 1')

    dgEbFlag = cur.fetchone()[0]

    conn.close()
    logging.info('******')
    logging.info('dgorEB   ' + str(dgEbFlag))
    return dgEbFlag.encode('utf8')


def storeDgEbFlag(dgEbFlag):
    conn = sqlite3.connect('db/dgOrEbDatabase.db')
    cur = conn.cursor()
    currDate = str(datetime.datetime.now())

    cur.execute('insert into dgEbFlagTable values (?,?)', [dgEbFlag,currDate])


    # dgEbFlag =str(cur.fetchone())
    conn.commit()
    conn.close()
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


    