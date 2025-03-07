@startuml
actor "User" as user

left to right direction

package App {
usecase "Select category" as slCat
usecase "Find restaurant" as findRes
usecase "View offer" as viewOff
usecase "Select Restaurant" as selRes
usecase "View Food" as viewFood
usecase "Share Restaurant" as shareRes
usecase "Select Food Option" as selFoodOption
usecase "Add to Cart" as addToCart
usecase "Select Delivery Option" as selDelOption
usecase "Edit location" as editLoc
usecase "Place Delivery" as placeDel
usecase "Review" as review
usecase "View Orders" as viewOrd
usecase "View All Carts" as viewAllCarts
usecase "Select Payment Method"  as selPayment
usecase "View Order" as total
usecase "Use Promotion" as usePromo
}

user -- slCat
user -- findRes
user -- selRes
user -- viewOff
user -- viewOrd
user -- total
user -- viewAllCarts

viewFood <.. selRes : include
selFoodOption ..> viewFood : extend
addToCart ..> selFoodOption : extend
selDelOption ..> total : extend
editLoc ..> total : extend
placeDel <.. total : include
review <.. placeDel : include
selPayment ..> total : extend

addToCart ..> viewFood : extend
shareRes ..> selRes : extend

total <.. addToCart : include
usePromo ..> total : extend

total ..> viewAllCarts : extend
@enduml