import { API_URL } from '../Config/config';

const Subscription = () => {
    return (
        <>
            <h1>Subscription</h1>
            <div className='subscription'>
                <div className='starter-div' >
                    <h2>Starter plan</h2>
                    <img className='month-img' src='https://img.freepik.com/free-vector/subscriber-concept-illustration_114360-3453.jpg?t=st=1654685116~exp=1654685716~hmac=b67fdd003003bc4f477b5184b2201a36a5a88ebefc2552ee7f4f723a2acef85f&w=740'></img>

                    <form action={`${API_URL}/subscription/create-subscription/`} method="POST">
                        <input type="hidden" name="lookup_key" value="Starterkey" />
                        <button className="btn-month" type="submit" >&#8377;30 / Month</button>
                    </form>
                </div>
                <br></br>
                <div className='premium-div'>
                    <h2>Premium plan</h2>
                    <img className='year-img' src='https://img.freepik.com/free-vector/subscriber-concept-illustration_114360-2949.jpg?t=st=1654651458~exp=1654652058~hmac=fc1ea117f4198608284f1fea2f5af8f4c50f75692b80c711ad5c93793d0f3ab0&w=740'></img>
                    <form action={`${API_URL}/subscription/create-subscription/`} method="POST">
                        <input type="hidden" name="lookup_key" value="Premiumplankey" />
                        <button className="btn-year" type="submit" >&#8377;350 /Year</button>
                    </form>
                </div>

            </div>
            <br>
            </br>
        </>
    );
}

export default Subscription;