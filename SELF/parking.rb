class Parking
    # To debug
    def printAll()
        puts @s_available
        puts @m_available
        puts @l_available
        puts @all_map
    end

    def initialize(x,y,z)

        @s_available=Hash.new
        (1..x).map{|i| @s_available[i]=""}
        
        @m_available=Hash.new
        (1..y).map{|i| @m_available[i]=""}
       
        @l_available=Hash.new
        (1..z).map{|i| @l_available[i]=""}
 
        @all_map = Hash.new
        
    end
    
    def admitTheCar (licensePlatNumber,carsize) 
        if @all_map.key?(licensePlatNumber)
            return "Faliure"
        end
        if carsize=='small' && @s_available.size!=0
            key, value = @s_available.first
           
            @s_available.delete(key)
            @all_map[licensePlatNumber]=['s',key]
            return "Success"

        elsif (carsize=='small' || carsize=='medium') && @m_available.size!=0
            key, value = @m_available.first
           
            @m_available.delete(key)
            @all_map[licensePlatNumber]=['m',key]
            return "Success"

        elsif (carsize=='small' || carsize=='medium'|| carsize=='large') && @l_available.size!=0
            key, value = @l_available.first
            # @l_occupied[key]=licensePlatNumber
            @l_available.delete(key)
            @all_map[licensePlatNumber]=['l',key]
            return "Success"

        else
            return "Faliure"
        end
    end

    def exitTheCar(licensePlatNumber)
        if @all_map.key?(licensePlatNumber)
            size=@all_map[licensePlatNumber][0]
            id=@all_map[licensePlatNumber][1]
            if size=='s'
                @s_available[id]=""
                
            elsif size=='m'
                @m_available[id]=""
               
            else
                @l_available[id]=""
               
            end
            @all_map.delete(licensePlatNumber)
            return "Success"
        end
        return "Faliure"
    end

end

menu_option = "1"
puts "Enter number of small parkings"
x=gets.to_i
puts "Enter number of medium parkings"
y=gets.to_i
puts "Enter number of large parkings"
z=gets.to_i

obj= Parking. new(x,y,z)
while menu_option=="1" || menu_option=="2" || menu_option=="3"
    # To debug the code please uncomment the next line
    # obj.printAll()
    puts "\n1. Admit Car\n2. Exit Car\n3. Exit Menu"
    menu_option = gets.chomp
    puts `clear`
    if menu_option=="1"
        puts "Enter License Plate Number"
        licensePlatNumber=gets.chomp
        puts "Enter Car Size (small, medium, large)"
        carsize=gets.chomp
        puts ""
        puts obj.admitTheCar(licensePlatNumber,carsize)

    elsif menu_option=="2"
        puts "Enter License Plate Number"
        licensePlatNumber=gets.chomp
        puts ""
        puts obj.exitTheCar(licensePlatNumber)
    elsif menu_option=="3"
        break
    end

end
