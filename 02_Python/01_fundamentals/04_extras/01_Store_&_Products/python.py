import product as pt
import store as st


if __name__ == "__main__":   
    
    store1 = st.store("Compu store")    
    compu = pt.product('Computer', 1000, "tecno")
    radio = pt.product('Radio', 70, 'sound')
    tablet = pt.product('Tablet', 150, "mobile")

    store1.add_product(compu)
    store1.add_product(radio)
    store1.add_product(tablet)

    compu.print_info()
    radio.print_info()



    store1.sales(0.1)
    store1.print_prod()
    store1.sell_product(0)
    store1.print_prod()