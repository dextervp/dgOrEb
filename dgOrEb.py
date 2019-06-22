import sqlite3
import datetime

def getDgEbFlag():
    print 'one'
    conn = sqlite3.connect('db/dgOrEBDatabase.db')
    cur = conn.cursor()
    # print 'con ' + conn
    cur.execute('select dgEbFlag from dgEbFlagTable order by create_tmstp desc limit 1')

    dgEbFlag = cur.fetchone()[0]

    conn.close()
    print '******'
    print dgEbFlag
    return dgEbFlag.encode('utf8')


def storeDgEbFlag(dgEbFlag):
    conn = sqlite3.connect('db/dgOrEBDatabase.db')
    cur = conn.cursor()
    currDate = str(datetime.datetime.now())

    cur.execute('insert into dgEbFlagTable values (?,?)', [dgEbFlag,currDate])

    # dgEbFlag =str(cur.fetchone())
    conn.commit()
    conn.close()


def main():
    dgEbFlag = getDgEbFlag()
    print 'flag ' + dgEbFlag
    if dgEbFlag == 'EB':
        dgEbFlag = 'DG'
    elif dgEbFlag == 'DG':
        dgEbFlag = 'EB'

    storeDgEbFlag(dgEbFlag)


if __name__ == '__main__':
    main()


    