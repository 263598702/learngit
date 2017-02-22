using Microsoft.Owin;
using Owin;

[assembly: OwinStartupAttribute(typeof(hxWeb.Startup))]
namespace hxWeb
{
    public partial class Startup
    {
        public void Configuration(IAppBuilder app)
        {
            ConfigureAuth(app);
        }
    }
}
