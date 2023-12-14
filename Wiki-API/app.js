const express = require("express");
const bodyParser = require("body-parser");
const ejs = require("ejs");
const mongoose = require('mongoose');

const app = express();

app.set('view engine', 'ejs');

app.use(bodyParser.urlencoded({
  extended: true
}));
app.use(express.static("public"));


// mongoose.connect("mongodb://localhost:27017/wikiDB", {useNewUrlParser: true});
async function main() {
    await mongoose.connect('mongodb://127.0.0.1:27017/wikiDB');
}
main().catch(err => console.log(err));

// const articleSchema = {
//     title: String,
//     content: String
// }
const articleSchema = new mongoose.Schema({
    title: String,
    content: String
});

const Article = mongoose.model("Article", articleSchema);

// app.get('/articles', function (req, res) {
//     Article.find(function (err, foundArticles) {
//          res.send(foundArticles);
//     })
// })
app.get("/articles", async(req,res)=>{
    try{
    const foundArticles= await Article.find();
        // console.log(foundArticles);
        res.send(foundArticles);
    }catch(err){
        // console.log(err);
        res.send(err);
    }
});

// app.post('/articles', async(req,res)=>{
app.post('https://cyt8g2-3000.csb.app/articles', async(req,res)=>{
    
    try {
        console.log(req.body.title);
        console.log(req.body.content);
        const newArticle = new Article({
            title: req.body.title,
            content: req.body.content
        });
        newArticle.save();
    }
    catch (err){
        res.send(err);
    }

    // newArticle.save(async (err) => {
    //     if (!err) res.send("Successfully added a new article.");
    //     else res.send(err);
    // });
});

app.delete('/articles', async (req, res) => {
    // try {
    //     Article.deleteMany();
    // }
    // catch (err) {
    //     res.send(err);
    // }
    Article.deleteMany(async (err) => {
        if (!err) res.send("Successfully deleted all articles.");
        else res.send(err);
    })
});

app.listen(3000, function() {
  console.log("Server started on port 3000");
});