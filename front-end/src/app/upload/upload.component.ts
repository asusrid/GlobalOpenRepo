import { Component, OnInit, ElementRef, HostListener } from '@angular/core';
import { FormBuilder, FormGroup, Validators, FormControl } from '@angular/forms';
import { HttpClient, HttpEvent, HttpEventType, HttpResponse } from '@angular/common/http';
import { pipe } from 'rxjs';
import { filter, map, tap } from 'rxjs/operators';

@Component({
  selector: 'app-upload',
  templateUrl: './upload.component.html',
  styleUrls: ['./upload.component.css']
})
export class UploadComponent implements OnInit {

  uploadFileForm: FormGroup;
  file: File | null = null;
  submitted = false;
  progress = 0;
  uri:string;

  @HostListener('change', ['$event.target.files']) emitFiles( event: FileList ) {
    const file = event && event.item(0);
    this.file = file;
  }

  constructor(private formBuilder: FormBuilder, private http: HttpClient, private host: ElementRef<HTMLInputElement>) {
  	this.uri = 'http://192.168.1.125:3000';
  }

  ngOnInit(): void {
  	this.uploadFileForm = this.formBuilder.group({
      email: ['admin@admin', Validators.required],
      password: ['admin', Validators.required],
      file: ['', Validators.required]
    });
  }

  get f() { return this.uploadFileForm.controls; }

  public saveFile() {
      this.submitted = true;

      // stop the process here if form is invalid
      if (this.uploadFileForm.invalid) {
        return;
      }

      if(this.uploadFileForm.get('email').value == 'admin@admin')
      console.log(this.file);
      console.log('SUCCESS!!');
      console.log(this.uploadFileForm.get('course').value);
      this.http.post(`${this.uri}/videos`, this.toFormData(this.uploadFileForm.value),
          {reportProgress: true, observe: 'events'}
      ).pipe(
          this.uploadProgress(progress => (this.progress = progress)),
          this.toResponseBody()
      ).subscribe((data: any) => {
          this.progress = 0;
          //this.uploadFileForm.reset();
          // do something with the response
      }, (error: any) => {
          console.log(error);
      });
  }

  public toFormData<T>( formValue: T ) {
    const formData = new FormData();

    for ( const key of Object.keys(formValue) ) {
      const value = formValue[key];
      formData.append(key, value);
    }
    formData.append('video', this.file, this.file.name);
    return formData;
  }

  public toResponseBody<T>() {
      return pipe(
          filter((event: HttpEvent<T>) => event.type === HttpEventType.Response),
          map((res: HttpResponse<T>) => res.body)
      );
  }

  public uploadProgress<T>( cb: ( progress: number ) => void ) {
    return tap(( event: HttpEvent<T> ) => {
      if ( event.type === HttpEventType.UploadProgress ) {
        cb(Math.round((100 * event.loaded) / event.total));
      }
    });
  }
}
