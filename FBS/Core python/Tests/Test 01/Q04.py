### Q4. Calculate the cost of painting the following building’s walls (both interior and
# exterior). You need to accept area (one wall) and cost of both interior and exterior wall.
# (Note: 1. Below diagram is of two joint rooms.
# 2. It is upper view of building.)

def painting_cost (area, interior, exterior):
    interior_cost =( area * interior )
    exterior_cost =( area * exterior )
    
    total_cost = (interior_cost + exterior_cost)
    
    print("Interior Painting Cost =", interior_cost)
    print("Exterior Painting Cost =", exterior_cost)
    print("Total Painting Cost =", total_cost)
    
a = int(input("Enter area of one wall :"))
i = int(input("Enter interior wall cost :"))
e = int(input("Enter exterior wall cost :"))

painting_cost(a, i, e)