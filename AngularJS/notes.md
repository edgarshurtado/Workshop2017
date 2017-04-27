## Set a value from ng-click inside an ng-repeat

This doesn't work
```html
<div class="content-with-top-margin">
    <h2>Galería de fotos {{selected}}</h2>

    <div class="galery-row">
        <div class="photo-card-holder col-xs-6" ng-repeat="photo in photos">
            <img src="photos/{{photo}}" alt="" ng-click="selected = 2">
        </div>
    </div>
</div>
```

This, however, does:

```html
<div class="content-with-top-margin">
    <h2>Galería de fotos</h2>
    <div class="galery-row">
        <div class="photo-card-holder col-xs-6" ng-repeat="photo in photos">
            <img src="photos/{{photo}}" alt="" ng-click="setSelected(photo)">
        </div>
    </div>
</div>
```

```js

myApp.controller("galeriaController", ["$scope", function($scope){
    $scope.setSelected = function(photoSelected){
        $scope.selected = photoSelected;
    }
}]);
```

With this experience the conclusion is that is better to set values through 
functions rather than directly from the view.
