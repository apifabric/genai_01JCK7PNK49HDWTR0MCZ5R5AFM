import { MenuRootItem } from 'ontimize-web-ngx';

import { InventoryCardComponent } from './Inventory-card/Inventory-card.component';

import { StoreCardComponent } from './Store-card/Store-card.component';

import { StoreInventoryCardComponent } from './StoreInventory-card/StoreInventory-card.component';

import { SupplierCardComponent } from './Supplier-card/Supplier-card.component';

import { SupplierWoodCardComponent } from './SupplierWood-card/SupplierWood-card.component';

import { WoodCardComponent } from './Wood-card/Wood-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'Inventory', name: 'INVENTORY', icon: 'view_list', route: '/main/Inventory' }
    
        ,{ id: 'Store', name: 'STORE', icon: 'view_list', route: '/main/Store' }
    
        ,{ id: 'StoreInventory', name: 'STOREINVENTORY', icon: 'view_list', route: '/main/StoreInventory' }
    
        ,{ id: 'Supplier', name: 'SUPPLIER', icon: 'view_list', route: '/main/Supplier' }
    
        ,{ id: 'SupplierWood', name: 'SUPPLIERWOOD', icon: 'view_list', route: '/main/SupplierWood' }
    
        ,{ id: 'Wood', name: 'WOOD', icon: 'view_list', route: '/main/Wood' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    InventoryCardComponent

    ,StoreCardComponent

    ,StoreInventoryCardComponent

    ,SupplierCardComponent

    ,SupplierWoodCardComponent

    ,WoodCardComponent

];