
# rotors and reflectors mapping data
Beta = {'A':'L', 'B':'E', 'C':'Y', 'D':'J', 'E':'V', 'F':'C', 'G':'N', 'H':'I', 'I':'X', 'J':'W', 'K':'P', 'L':'B', 'M':'Q', 'N':'M', 'O':'D', 'P':'R', 'Q':'T', 'R':'A', 'S':'K', 'T':'Z', 'U':'G', 'V':'F', 'W':'U', 'X':'H', 'Y':'O', 'Z':'S'}

Gamma = {'A':'F', 'B':'S', 'C':'O', 'D':'K', 'E':'A', 'F':'N', 'G':'U', 'H':'E', 'I':'R', 'J':'H', 'K':'M', 'L':'B', 'M':'T', 'N':'I', 'O':'Y', 'P':'C', 'Q':'W', 'R':'L', 'S':'Q', 'T':'P', 'U':'Z', 'V':'X', 'W':'V', 'X':'G', 'Y':'J', 'Z':'D'}

I = {'A':'E', 'B':'K', 'C':'M', 'D':'F', 'E':'L', 'F':'G', 'G':'D', 'H':'Q', 'I':'V', 'J':'Z', 'K':'N', 'L':'T', 'M':'O', 'N':'W', 'O':'Y', 'P':'H', 'Q':'X', 'R':'U', 'S':'S', 'T':'P', 'U':'A', 'V':'I', 'W':'B', 'X':'R', 'Y':'C', 'Z':'J'}

II = {'A':'A', 'B':'J', 'C':'D', 'D':'K', 'E':'S', 'F':'I', 'G':'R', 'H':'U', 'I':'X', 'J':'B', 'K':'L', 'L':'H', 'M':'W', 'N':'T', 'O':'M', 'P':'C', 'Q':'Q', 'R':'G', 'S':'Z', 'T':'N', 'U':'P', 'V':'Y', 'W':'F', 'X':'V', 'Y':'O', 'Z':'E'}

III = {'A':'B', 'B':'D', 'C':'F', 'D':'H', 'E':'J', 'F':'L', 'G':'C', 'H':'P', 'I':'R', 'J':'T', 'K':'X', 'L':'V', 'M':'Z', 'N':'N', 'O':'Y', 'P':'E', 'Q':'I', 'R':'W', 'S':'G', 'T':'A', 'U':'K', 'V':'M', 'W':'U', 'X':'S', 'Y':'Q', 'Z':'O'}

IV = {'A':'E', 'B':'S', 'C':'O', 'D':'V', 'E':'P', 'F':'Z', 'G':'J', 'H':'A', 'I':'Y', 'J':'Q', 'K':'U', 'L':'I', 'M':'R', 'N':'H', 'O':'X', 'P':'L', 'Q':'N', 'R':'F', 'S':'T', 'T':'G', 'U':'K', 'V':'D', 'W':'C', 'X':'M', 'Y':'W', 'Z':'B'}

V = {'A':'V', 'B':'Z', 'C':'B', 'D':'R', 'E':'G', 'F':'I', 'G':'T', 'H':'Y', 'I':'U', 'J':'P', 'K':'S', 'L':'D', 'M':'N', 'N':'H', 'O':'L', 'P':'X', 'Q':'A', 'R':'W', 'S':'M', 'T':'J', 'U':'Q', 'V':'O', 'W':'F', 'X':'E', 'Y':'C', 'Z':'K'}

A = {'A':'E', 'B':'J', 'C':'M', 'D':'Z', 'E':'A', 'F':'L', 'G':'Y', 'H':'X', 'I':'V', 'J':'B', 'K':'W', 'L':'F', 'M':'C', 'N':'R', 'O':'Q', 'P':'U', 'Q':'O', 'R':'N', 'S':'T', 'T':'S', 'U':'P', 'V':'I', 'W':'K', 'X':'H', 'Y':'G', 'Z':'D'}

B = {'A':'Y', 'B':'R', 'C':'U', 'D':'H', 'E':'Q', 'F':'S', 'G':'L', 'H':'D', 'I':'P', 'J':'X', 'K':'N', 'L':'G', 'M':'O', 'N':'K', 'O':'M', 'P':'I', 'Q':'E', 'R':'B', 'S':'F', 'T':'Z', 'U':'C', 'V':'W', 'W':'V', 'X':'J', 'Y':'A', 'Z':'T'}

C = {'A':'F', 'B':'V', 'C':'P', 'D':'J', 'E':'I', 'F':'A', 'G':'O', 'H':'Y', 'I':'E', 'J':'D', 'K':'R', 'L':'Z', 'M':'X', 'N':'W', 'O':'G', 'P':'C', 'Q':'T', 'R':'K', 'S':'U', 'T':'Q', 'U':'S', 'V':'B', 'W':'N', 'X':'M', 'Y':'H', 'Z':'L'}

ref = {'A':'F', 'B':'V', 'C':'P', 'D':'J', 'E':'I', 'F':'A', 'G':'O', 'H':'Y', 'I':'E', 'J':'D', 'K':'R', 'L':'Z', 'M':'X', 'N':'W', 'O':'G', 'P':'C', 'Q':'T', 'R':'K', 'S':'U', 'T':'Q', 'U':'S', 'V':'B', 'W':'N', 'X':'M', 'Y':'H', 'Z':'L'}

class PlugLead:
    def __init__(self, mapping):
        self.cipher = {}
        if len(mapping) > 1:
            self.cipher[mapping[0]] = mapping[1]
            self.cipher[mapping[1]] = mapping[0]

    def encode(self, character):
        # check if the character has an encoding value
        value = self.cipher.get(character, 0)
        if  value != 0:
            return value
        else:
            return character


class Plugboard:
    def __init__(self):
        self.leads = []

    def add(self, lead):
        # ensuring max 10 leads
        if len(self.leads) == 10:
            raise ValueError ('Maximum allowed leads are 10')
        else:
            self.leads.append(lead)

    def encode(self, char):
        for lead in self.leads:
            value = lead.cipher.get(char, 0)
            if value != 0:
                return value
        return char

class rotor_from_name:
   
    types = {'BETA': Beta, 'GAMMA': Gamma, 'I': I, 'II': II, 'III': III, 'IV': IV, 'V': V, 'A': A, 'B': B, 'C': C, 'REF': ref}

    notches = {'I': 'Q', 'II': 'E', 'III': 'V', 'IV': 'J', 'V': 'Z'}

    def __init__(self, type, ring, pos):
        # ensuring proper inputs for rotors types, initial positions and ring settings
        try:
            type = type.upper()
            pos = pos.upper()
        except:
            raise ValueError ('Invalid rotor or position name!')

        if type not in rotor_from_name.types.keys():
            raise ValueError ('Invalid rotor name!')

        try:
            ring = int(ring)
        except:
            raise ValueError ('Invalid rotor ring, position or location input!')

        if ring < 0:
            raise ValueError ('Invalid rotor ring, position or location input!')
        
        self.type = type
        self.pos = pos
        self.ring = ring
        notch = rotor_from_name.notches.get(type, 'NA')
        self.notch = notch
        # total offset resulted from the ring and the rotation of the rotor
        self.offset = ord(pos) - ord('A') - (ring - 1)
        self.map = rotor_from_name.types[type]

    def encode_right_to_left(self, char):
        try:
            char = char.upper()
        except:
            raise ValueError ('Invalid letter to encrypt!')
        cipher = self.map.get(char, 0)
        if cipher == 0:
            raise ValueError ('Invalid letter to encrypt!')
        else:
            return cipher    
        
    def encode_left_to_right(self, char):
        try:
            char = char.upper()
        except:
            raise ValueError ('Invalid letter to encrypt!')

        if char not in self.map.values():
            raise ValueError ('Invalid letter to encrypt!')
        else:
            for key, value in self.map.items():
                if char == value:
                    return key

    def update(self):
        # rotates the rotor by 1 letter then updates the position and offset
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        char_pos = alpha.find(self.pos)
        # A-Z mapping
        if char_pos == 25:
            char_pos = -1
        # update rotor position
        self.pos = alpha[char_pos + 1]
        # update rotor offset
        self.offset = ord(self.pos) - ord('A') - (self.ring - 1)    
        
    def offset_input(self, char):
        # offset the input signal based on the rotor's rotation
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        char_pos = alpha.find(char)
        new_pos = char_pos + self.offset
        # Z-A mapping
        while new_pos > 25:
            new_pos = new_pos - 26        
            
        while new_pos < 0:
            new_pos = new_pos + 26
        
        return alpha[new_pos]    
    
    def offset_output(self, char):
        # offset the output signal based on the rotor's rotation
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        char_pos = alpha.find(char)
        new_pos = char_pos - self.offset
        # Z-A mapping
        while new_pos > 25:
            new_pos = new_pos - 26
        while new_pos < 0:
            new_pos = new_pos + 26
        return alpha[new_pos]



class Enigma:
    # Enigma object holds the rotors and plugboard data
    rotors = []
    plugboard = []

    # setting the rotors of the Enigma
    def set_enigma(self, types, ref, ring_settings, rotors_pos):
        types = types.split(' ')
        rings = ring_settings.split(' ')
        pos = rotors_pos.split(' ')
        n = len(types)
        if n != len(rings) or n != len(pos):
            raise ValueError ('inconsistent rotors inputs')

        if n != 3 and n != 4:
            raise ValueError ('Number of rotors must be 3 or 4!')

        rotors = []
        # adding the reflector
        rotor = rotor_from_name(ref, 1, 'A')
        rotors.append(rotor)
        # adding the rotors
        for i in range(n):
            rotor = rotor_from_name(types[i], rings[i], pos[i])
            rotors.append(rotor)

        rotors = list(reversed(rotors))
        self.rotors = rotors

    def encode_message(self, message):
        # encode or decode a message given the Enigma settings
        cipher = []
        n = len(self.rotors)
        for char in message:
            # char is not an alphabet letter
            if not char.isalpha():
                cipher.append(char)
                continue          

            char = self.plugboard.encode(char)
            notch0 = self.rotors[0].notch
            notch1 = self.rotors[1].notch

            # if the second rotor is on notch then all the three rotors will rotate
            if self.rotors[1].pos == notch1:
                self.rotors[0].update() 
                self.rotors[1].update() 
                self.rotors[2].update() 
            # if the first rotor is on notch then the first two rotors will rotate
            elif self.rotors[0].pos == notch0:
                self.rotors[0].update() 
                self.rotors[1].update()
            # only the first rotor will rotate
            else:
                self.rotors[0].update()

            # encoding the char through the different rotors from right to left
            in_char, encoded_char, out_char, input = '', '', '', char
            for i in range(n):
                rotor = self.rotors[i]
                in_char = rotor.offset_input(input)
                encoded_char = rotor.encode_right_to_left(in_char)
                out_char = rotor.offset_output(encoded_char)
                input = out_char        
            
            # encoding the char through the different rotors from left to right
            for i in range(n - 2, -1, -1):
                rotor = self.rotors[i]
                in_char = rotor.offset_input(input)
                encoded_char = rotor.encode_left_to_right(in_char)
                out_char = rotor.offset_output(encoded_char)
                input = out_char

            # adding the coded letter to the cipher message
            input = self.plugboard.encode(input)
            cipher.append(input)

        return ''.join(cipher)
                
    def initialize_board(self, string):
        # creates the plugboard data for the Enigma
        leads = string.split(' ')
        if len(leads) > 10:
            raise ValueError ("Maximum number of leads can't exceed 10!")

        plugboard = Plugboard()
        for lead in leads:
            plugboard.add(PlugLead(lead))

        #return plugboard
        self.plugboard = plugboard
                  

if __name__ == "__main__":
    # test cases
    enigma = Enigma()
    enigma.set_enigma(types ='I II III', ref='B', ring_settings='01 01 01', rotors_pos='A A Z')
    enigma.initialize_board('')    
    assert(enigma.encode_message('A') == 'U')

    enigma = Enigma()
    enigma.set_enigma(types ='I II III', ref='B', ring_settings='01 01 01', rotors_pos='A A A')
    enigma.initialize_board('')
    assert(enigma.encode_message('A') == 'B')    
    
    enigma = Enigma()
    enigma.set_enigma(types ='I II III', ref='B', ring_settings='01 01 01', rotors_pos='Q E V')
    enigma.initialize_board('')
    assert(enigma.encode_message('A') == 'L')    
    
    enigma = Enigma()
    enigma.set_enigma(types ='IV V Beta', ref='B', ring_settings='14 09 24', rotors_pos='A A A')
    enigma.initialize_board('')
    assert(enigma.encode_message('H') == 'Y')    
    
    enigma = Enigma()
    enigma.set_enigma(types ='I II III IV', ref='C', ring_settings='07 11 15 19', rotors_pos='Q E V Z')
    enigma.initialize_board('')
    assert(enigma.encode_message('Z') == 'V')
    ###########################################################################
    enigma = Enigma()
    enigma.set_enigma(types ='I II III', ref='B', ring_settings='01 01 01', rotors_pos='A A Z')
    enigma.initialize_board('HL MO AJ CX BZ SR NI YW DG PK')
    assert(enigma.encode_message('RFKTMBXVVW') == 'HELLOWORLD')     
    
    enigma = Enigma()
    enigma.set_enigma(types ='IV V Beta I', ref='A', ring_settings='18 24 03 05', rotors_pos='E Z G P')
    enigma.initialize_board('PC XZ FM QA ST NB HY OR EV IU')
    print(enigma.encode_message('BUPXWJCDPFASXBDHLBBIBSRNWCSZXQOLBNXYAXVHOGCUUIBCVMPUZYUUKHI'))   
    ########################################################################
