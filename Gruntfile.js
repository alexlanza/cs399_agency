/*global module:false*/
module.exports = function (grunt) {

    // Project configuration.
    grunt.initConfig({
        // Task configuration.
        less: {
            development: {
                options: {
                },
                files: {
                    // target.css file: source.less file
                    "agency/static/css/bootstrap.css": "agency/static/css/less/bootstrap.less"
                }
            },
            production: {
                options: {
                    cleancss: true,
                    compress: true,
                    yuicompress: true,
                    optimization: 2
                },
                files: {
                    // target.css file: source.less file
                    "agency/static/css/bootstrap.min.css": "agency/static/css/less/bootstrap.less"
                }
            }
        },
        watch: {
            less: {
                files: ['agency/static/css/less/*', 'agency/static/css/less/mixins/*', 'Gruntfile.js'],
                tasks: ['less']
            }

        }
    });
    grunt.loadNpmTasks('grunt-contrib-less');
//    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-watch');
//    grunt.loadNpmTasks('grunt-contrib-concat');
//    grunt.loadNpmTasks('grunt-sloc');

    // Default task.
    grunt.registerTask('default', ['concat', 'uglify', 'less', 'sloc']);

};