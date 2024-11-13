import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './StoreInventory-card.component.html',
  styleUrls: ['./StoreInventory-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.StoreInventory-card]': 'true'
  }
})

export class StoreInventoryCardComponent {


}