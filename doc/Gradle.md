```
file:Gradle
title:gradle使用
date:2016/07/13
tags:gradle
```
# Gradle使用方法
```
//root build.gradle
def retrofitVersion = "2.0.2"
def okHttpVersion = '3.2.0'

project.ext {
    libRetrofit = "com.squareup.retrofit2:retrofit:${retrofitVersion}"
    libRetrofitConverterGson = "com.squareup.retrofit2:converter-gson:${retrofitVersion}"
    libRetrofitAdapterRxJava = "com.squareup.retrofit2:adapter-rxjava:${retrofitVersion}"
    libOkHttpLoggingInterceptor = "com.squareup.okhttp3:logging-interceptor:${okHttpVersion}"
}
//module build.gradle
dependencies {
    compile rootProject.ext.libRetrofit
    compile rootProject.ext.libRetrofitConverterGson
    compile rootProject.ext.libRetrofitAdapterRxJava
    compile rootProject.ext.libOkHttpLoggingInterceptor
}
```
