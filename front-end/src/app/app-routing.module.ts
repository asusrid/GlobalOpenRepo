import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { IndexComponent } from './index/index.component';
import { UploadComponent } from './upload/upload.component';
import { AttributesComponent } from './attributes/attributes.component';


const routes: Routes = [
	{path: '', component: IndexComponent},
	{path: 'upload', component: UploadComponent},
	{path: 'design', component: AttributesComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
