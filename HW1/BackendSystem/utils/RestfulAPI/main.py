import traceback

import uvicorn
from fastapi import FastAPI, Depends

from BackendSystem.submission_system import SubmissionSystem
from BackendSystem.utils.RestfulAPI.query_parameter import PostDetail

app = FastAPI()


@app.get("/api/posting_system/receive/{post_id}")
async def predict(post_id: int):
    try:
        suggestion_room_list = submission.execute(post_id=int(post_id))
        return suggestion_room_list
    except Exception as e:
        traceback.print_exc()
        return []


@app.get("/api/posting_system/submission/{description}")
async def predict(post_detail: PostDetail = Depends()):
    try:
        return submission.execute(description=post_detail.description,
                                  photo_url=post_detail.photoURL,
                                  email_address=post_detail.emailAddress
                                  )
    except Exception as e:
        traceback.print_exc()
        return []


if __name__ == '__main__':
    submission = SubmissionSystem()
    uvicorn.run(app, host="localhost", port=8484)
