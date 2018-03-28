db.setlists.find({"setlist": "Breath In"}).forEach(function(doc){
   var setlist = doc.setlist;
  for(var i in setlist) {
   if (setlist[i] = "Breath In") {

      setlist[i] = "Breathe In";
    }
  }
 db.setlists.update({"_id": doc._id}, {$set:{"setlist": setlist}})
});