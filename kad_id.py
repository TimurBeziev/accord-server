class KadId:
    @staticmethod
    def distance(lhs_id, rhs_id):
        return lhs_id^rhs_id
    
    @staticmethod
    def compare_ref(lhs_id, rhs_id, ref) -> int:
        lhs_dist = KadId.distance(lhs_id, ref)
        rhs_dist = KadId.distance(rhs_id, ref)
        if lhs_dist < rhs_dist:
            return -1
        if lhs_dist > rhs_dist:
            return 1
        return 0

    @staticmethod
    def compare_exp(lhs_id, rhs_id) -> int:
        dist = KadId.distance(lhs_id, rhs_id)
        bit = 0
        while dist > 1:
            bit += 1
            dist >>= 1
        return bit
        
    @staticmethod
    def __validate_id(id: int):
        assert id != None and id < 2**160, 'Invalid id'
 

