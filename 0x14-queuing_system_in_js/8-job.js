function createPushNotificationsJobs(jobs, queue) {
  if (Array.isArray(jobs) === false) {
    throw Error('Jobs is not an array');
  }

  jobs.forEach((job) => {
    const createdJob = queue.create('push_notification_code_3', job).save((err) => {
        if (!err) {
            console.log(`Notification job created: ${createdJob.id}`);
        }
    });

    createdJob.on('compelete', () => {
        console.log(`Notification job ${createdJob.id} completed`);
    });

    createdJob.on('failed', (err) => {
        console.log(`Notification job ${createdJob.id} failed: ${err}`);
    });

    createdJob.on('progress', (progress) => {
        console.log(`Notification job ${createdJob.id} ${progress} complete`);
    });
  });
}

export default createPushNotificationsJobs;