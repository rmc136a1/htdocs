function setcolor(color){
  var alist=document.querySelectorAll('a');
  var i=0;
  while(i<alist.length){
    alist[i].style.color=color;
    i=i+1;
  }
}
var links={
  setcolor:function(color){
    $('a').css('color',color);
  }
}
var body={
  setcolor:function (color){
    $('body').css('color',color);
  },
  setbackgroundcolor:function (color){
    $('body').css('backgroundColor',color);
  }
}
function nightdayhandeler(self){
  if(self.value==='night'){
    body.setbackgroundcolor('black');
    body.setcolor('white');
    self.value='day';

    links.setcolor('powderblue');
  }else{
    body.setbackgroundcolor('white');
    body.setcolor('black');
    self.value='night';

    links.setcolor('blue');
  }
}
