#!/usr/bin/yarn dev
import { createQueue } from 'kue';

const jobs = [
  {
    phoneNumber: '+2336474764',
    message: 'This is the code 1234 to verify your account',
  },
  {
    phoneNumber: '+23387634786',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '+23382347548',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '+233564356453',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '+233845647654',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '+233687346387',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '+23349587454',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '+23374336433',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '+233647443733',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '+233757484744',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '+233646757532',
    message: 'This is the code 4321 to verify your account',
  },
];

const queue = createQueue({ name: 'push_notification_code_2' });

for (const jobInfo of jobs) {
  const job = queue.create('push_notification_code_2', jobInfo);

  job
    .on('enqueue', () => {
      console.log('Notification job created:', job.id);
    })
    .on('complete', () => {
      console.log('Notification job', job.id, 'completed');
    })
    .on('failed', (err) => {
      console.log('Notification job', job.id, 'failed:', err.message || err.toString());
    })
    .on('progress', (progress, _data) => {
      console.log('Notification job', job.id, `${progress}% complete`);
    });
  job.save();
}