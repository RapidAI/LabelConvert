/*
 * Created by SharpDevelop.
 * User: He Tao
 * Date: 2015/7/2
 * Time: 15:13
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;

namespace Delegate
{
    // 热水器
    public class Heater
    {
        private int temperature;
        public string type = "RealFire 001"; // 添加型号作为演示
        public string area = "China Xian"; // 添加产地作为演示
        //声明委托
        public delegate void BoiledEventHandler(Object sender, BoliedEventArgs e);
        public event BoiledEventHandler Boiled;
        //声明事件
        // 定义BoliedEventArgs类，传递给Observer所感兴趣的信息
        public class BoliedEventArgs : EventArgs
        {
            public readonly int temperature;
            public BoliedEventArgs(int temperature)
            {
                this.temperature = temperature;
            }
        }
        // 可以供继承自 Heater 的类重写，以便继承类拒绝其他对象对它的监视
        protected virtual void OnBolied(BoliedEventArgs e)
        {
            if (Boiled != null) {       // 如果有对象注册
                Boiled(this, e);       // 调用所有注册对象的方法
            }
        }
              
        // 烧水。
        public void BoilWater()
        {
            for (int i = 0; i <= 100; i++) {
                temperature = i;
                if (temperature > 95) {
                    //建立BoliedEventArgs 对象。
                    BoliedEventArgs e = new BoliedEventArgs(temperature);
                    OnBolied(e);       // 调用 OnBolied方法
                }
            }
        }
    }
    // 警报器
    public class Alarm
    {
        public void MakeAlert(Object sender, Heater.BoliedEventArgs e)
        {
            Heater heater = (Heater)sender;              //这里是不是很熟悉呢？
            //访问 sender 中的公共字段
            Console.WriteLine("Alarm：{0} - {1}: ", heater.area, heater.type);
            Console.WriteLine("Alarm: 嘀嘀嘀，水已经 {0} 度了：", e.temperature); 
        }
    }
    // 显示器
    public class Display
    {
        public static void ShowMsg(Object sender, Heater.BoliedEventArgs e)
        {       //静态方法
            Heater heater = (Heater)sender;
            Console.WriteLine("Display：{0} - {1}: ", heater.area, heater.type);
            Console.WriteLine("Display：水快烧开了，当前温度：{0}度。", e.temperature);
        }
    }
    class Program
    {
        static void Main()
        {
            Heater heater = new Heater();
            Alarm alarm = new Alarm();
            heater.Boiled += alarm.MakeAlert;       //注册方法
            // heater.Boiled += (new Alarm()).MakeAlert;              //给匿名对象注册方法
            // heater.Boiled += new Heater.BoiledEventHandler(alarm.MakeAlert);   //也可以这么注册
            heater.Boiled += Display.ShowMsg;              //注册静态方法
            heater.BoilWater();       //烧水，会自动调用注册过对象的方法
            Console.ReadKey();
        }
    }
}


