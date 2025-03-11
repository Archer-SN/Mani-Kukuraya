@startuml
actor "User" as user

left to right direction

package App {
usecase "Select category" as slCat
usecase "Search restaurant" as findRes
usecase "View Promotions" as viewOff
usecase "Select Restaurant" as selRes
usecase "View Food" as viewFood
usecase "Select Food Option" as selFoodOption
usecase "Add to Cart" as addToCart
usecase "Select Delivery Option" as selDelOption
usecase "Place Delivery" as placeDel
usecase "Review" as review
usecase "View Carts" as viewOrd
usecase "View All Carts" as viewAllCarts
usecase "Select Payment Method"  as selPayment
usecase "View Order" as total
usecase "Use Promotion" as usePromo
usecase "View Food" as viewFood
usecase "Favorite Restaurant" as favoriteRestaurant
usecase "View Profile" as viewProfile
usecase "View Favorites" as viewFavorite

usecase "View Account Management" as viewManagement
usecase "Edit Username" as editUsername
usecase "Edit Password" as editPassword


usecase "View Locations" as viewLocation
usecase "Add Location" as addLocation
usecase "Edit Location" as editLocation

usecase "Make Payment" as makePayment
usecase "Change Location" as changeLocation

}

user -- slCat
user -- findRes
user -- selRes
user -- viewOff
user -- viewOrd
user -- total
user -- viewAllCarts
user -- viewFood
user -- viewProfile

viewProfile <.. viewManagement : extend
viewManagement <.. editPassword: extend
viewManagement <.. editUsername: extend

viewProfile <.. viewLocation : extend
viewLocation <.. addLocation: extend
viewLocation <.. editLocation: extend

viewProfile <.. viewFavorite : extend

findRes <.. selRes: extend


viewFood <.. selRes : include
selFoodOption ..> viewFood : extend
addToCart ..> selFoodOption : extend
selDelOption ..> total : extend
changeLocation ..> total : extend
placeDel <.. makePayment : include
makePayment <.. total : include
review <.. placeDel : include
selPayment ..> total : extend

addToCart ..> viewFood : extend
favoriteRestaurant ..> selRes : extend

total <.. addToCart : include
usePromo ..> total : extend

total ..> viewAllCarts : extend
@enduml