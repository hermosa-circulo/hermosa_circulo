var app = angular.module('portal',[]);
app.controller('portal_controller',fuction(){
    this.links  =[
        {name:'nasne',  url:'http://nasne.buttobi.com'},
        {name:'router', url:'http://router.buttibi.com'},
        {name:'home',   url:'https://portal.buttobi.com'}
    ];
});