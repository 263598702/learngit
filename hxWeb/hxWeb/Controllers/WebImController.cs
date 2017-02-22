using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace hxWeb.Controllers
{
    public class WebImController : Controller
    {
        // GET: WebIm
        public ActionResult Index(string token)
        {
            ViewBag.token = token;
            return View();
        }
    }
}