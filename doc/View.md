```
file:View
title:自定义View的使用方法
date:2016/05/29
tags:Android,View
```

# 自定义View

## 涉及知识
* 绘制过程  
http://blog.csdn.net/leejizhou/article/details/51524948

#  自定义控件
```
public class ScoreView extends View{
    //实现构造方法时传入要显示的数字
    public ScoreView(Context context,int score){
        super(context);
        init(score);
    }
    //初始化
    private void init(int score) {
      this.score=score;
      Resources res = getResources();
      //以10dp作为单位量
      unitage = res.getDimension(R.dimen.unitage);

      //初始黑色笔
      mPaint_black = new Paint();
      //设置抗锯齿，优化绘制效果的精细度
      mPaint_black.setAntiAlias(true);
      //设置图像抖动处理,也是用于优化图像的显示效果
      mPaint_black.setDither(true);
      //设置画笔的颜色
      mPaint_black.setColor(Color.BLACK);
      //设置画笔的风格为空心
      mPaint_black.setStyle(Paint.Style.STROKE);
      //设置“空心”的外框宽度为2dp
      mPaint_black.setStrokeWidth(unitage*0.2f);

      //初始白色笔
      mPaint_while = new Paint();
      mPaint_while.setAntiAlias(true);
      mPaint_while.setStyle(Paint.Style.STROKE);
      mPaint_while.setStrokeWidth(unitage*0.2f);
      mPaint_while.setDither(true);
      //设置文本的字号大小
      mPaint_while.setTextSize(unitage*6);
      //设置文本的对其方式为水平居中
      mPaint_while.setTextAlign(Paint.Align.CENTER);
      mPaint_while.setColor(Color.WHITE);

      //初始化圆弧所需条件（及设置圆弧的外接矩形的四边）
      mRectf = new RectF();
      mRectf.set(unitage*0.5f,unitage*0.5f,unitage*18.5f,unitage*18.5f);
      //设置整个控件的宽高配置参数
      setLayoutParams(new ViewGroup.LayoutParams((int)(unitage*19.5f),(int)(unitage*19.5f)));

      //获取该view的视图树观察者并添加绘制变化监听者
      //实现有绘制变化时的回调方法
      this.getViewTreeObserver().addOnPreDrawListener(new ViewTreeObserver.OnPreDrawListener() {
          @Override
          public boolean onPreDraw() {
              //2.开启子线程对绘制用到的数据进行修改
              new DrawThread();
              getViewTreeObserver().removeOnPreDrawListener(this);
              return false;
          }
      });
  }     
//开启子线程并在绘制监听的回调方法中实现实时更新绘制数据
  public class DrawThread implements Runnable {
   //2.开启子线程,并通过绘制监听实时更新绘制数据
   private final Thread mDrawThread;
   private int statek;
   int count;

   public DrawThread() {
       mDrawThread = new Thread(this);
       mDrawThread.start();
   }

   @Override
   public void run() {
       while (true) {
           switch (statek) {
               case 0://给一点点缓冲的时间
                   try {
                       Thread.sleep(200);
                       statek = 1;
                   } catch (InterruptedException e) {

                   }
                   break;
               case 1:
                   try {//更新显示的数据
                       Thread.sleep(20);
                       arc_y += 3.6f;
                       score_text++;
                       count++;
                       postInvalidate();
                   } catch (InterruptedException e) {
                       e.printStackTrace();
                   }
                   break;
           }
           if (count >= score)//满足该条件就结束循环
               break;
       }

   }
}
//重写onDraw方法
@Override
protected void onDraw(Canvas canvas) {
   super.onDraw(canvas);
   //绘制弧形
   //黑笔画的是一个整圆所有从哪里开始都一样
   canvas.drawArc(mRectf,0,360,false,mPaint_black);
   //白笔之所以从-90度开始，是因为0度其实使我们的3点钟的位置，所以-90才是我们的0点的位置
   canvas.drawArc(mRectf,-90,arc_y,false,mPaint_while);
   //绘制文本
   canvas.drawText(score_text+"",unitage*9.7f,unitage*11.0f,mPaint_while);

   //到此整个自定义View就已经写完了
}
//使用控件
public class ScoreActivity extends Activity {

    private LinearLayout scoreView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_score);
        scoreView = (LinearLayout) findViewById(R.id.score_View);
        scoreView.addView(new ScoreView(this,80));
    }
}
```
