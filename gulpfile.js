'use strict';

let gulp = require('gulp');
let rename = require('gulp-rename');
let sass = require('gulp-sass');
let uglify = require('gulp-uglify');

sass.compiler = require('node-sass');

gulp.task('minify-js', function () {
    return gulp.src(['static/**/*.js', '!static/**/*.min.js'])
      .pipe(uglify())
      .pipe(rename(function (path) {
          path.extname = '.min.js'
      }))
      .pipe(gulp.dest('static'));
});

gulp.task('minify-js:watch', function () {
    gulp.watch(['static/**/*.js', '!static/**/*.min.js'], gulp.series('minify-js'))
});

gulp.task('sass', function () {
  return gulp.src('static/**/main.scss')
    .pipe(sass({outputStyle: 'compressed'}).on('error', sass.logError))
    .pipe(gulp.dest('static'));
});

gulp.task('sass:watch', function () {
  gulp.watch('static/**/*.scss', gulp.series('sass'));
});

gulp.task('default', gulp.parallel('minify-js:watch', 'sass:watch'));