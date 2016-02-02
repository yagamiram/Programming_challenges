        '''
        This program is to store the records efficiently and retrieve the last occurance of the record.
        Everything happens in O(1) complexity (retrieving the last occurance of the same record)
        How ?
        Using namedtuple and defaultdict
        namedtuple - A memory efficient light weigh object without __dir__ in its class.
        It's factory class and creates a class object as you like
        Here there are so many records, and for each record an object called Person is created
        The attributes of the person object is name, money, loc, min
        The Person is object is created using name tuple
        And the attributes are accessed like: Person.name, Person.money, Person.loc, Person.min
        
        Now defauldict is used to store the record's index positon to retrieve it whenever needed.
        What is default dict ?
        A better approach than normal dict. If wont return KEYERROR anytime. which means, the key
        will created and assigned to the default value.
        A default dict can be created to keys whos values are lists,sets, dicts etc
        
        Here lookup table is dict which contains only key - name
        The Key - name is a default dict who's key is the name of the person and value is the index of occurance of the person
        in the input records.
        
        ex: Lookup_table = {'name': {'TK':0, 'Sri':1, 'Jessi': 2}}
        '''
        from collections import defaultdict, namedtuple
        class DB(object):
            def __init__(self, input_records, record_names):
                self.fields = ['name','money','loc','min']
                self.Record = namedtuple(record_names, self.fields)
                self.records = list()
                self.suspicious = list()
                for each_record in input_records:
                    row = each_record.split("|")
                    self.records.append(self.Record(*row))
                self.lookup_table = dict()
                self.lookup_table = {'name' : defaultdict(lambda : -1)}
                for index, record in enumerate(self.records):
                    value = getattr(record, 'name')
                    # check if the money is greater than 3000$
                    if value not in self.suspicious:
                        if int(getattr(record, 'money')) > 3000:
                            self.suspicious.append(value)
                            continue
                        # check if the same person has done a transaction in less than 1 hr in different location
                        index_value = self.lookup_table['name'].get(value, -1)
                        print "index value is", index_value
                        if index_value >= 0:
                            # record is found
                            person_record = self.records[index_value]
                            if person_record.loc != record.loc and abs(int(person_record.min) - int(record.min)) > 60:
                                self.suspicious.append(value)
                                continue
                        self.lookup_table['name'][value] = index
                        print self.lookup_table
                print self.suspicious
        if __name__ == "__main__":
            input_records = ['shilpa|500|california|63',
                            'tom|25|new york|615','krasi|9000|california|1230',
                            'tom|25|new york|1230','tom|25|new york|1238',
                            'shilpa|50|michigan|1300','matt|900000|georgia|1305',
                            'jay|100000|virginia|1310',
                            'krasi|49|florida|1310']
            db = DB(input_records, 'Person')
